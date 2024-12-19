use clap::{Parser, Subcommand};
use std::process::{Command, Stdio};

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
pub struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand, Debug)]
enum Commands {
    Solve {
        /// The number to solve for
        #[arg(short, long)]
        number: u16,
    },
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Commands::Solve { number } => {
            let cmd_args = vec!["run".to_string(), "--bin".to_string(), number.to_string()];

            let mut cmd = Command::new("cargo")
                .args(&cmd_args)
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .spawn()
                .unwrap();

            cmd.wait().unwrap();
        }
    }
}
