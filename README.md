# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 413
- HTTP: 127 alive / 77 gold
- HTTPS: 150 alive / 21 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40242
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
