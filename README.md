# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 428
- HTTP: 100 alive / 77 gold
- HTTPS: 117 alive / 17 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42470
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
