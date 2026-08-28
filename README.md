# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 423
- HTTP: 96 alive / 73 gold
- HTTPS: 122 alive / 20 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42490
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
