# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 425
- HTTP: 107 alive / 77 gold
- HTTPS: 129 alive / 16 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42475
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
