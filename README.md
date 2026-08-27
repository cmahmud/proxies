# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 417
- HTTP: 128 alive / 72 gold
- HTTPS: 176 alive / 22 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40488
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
