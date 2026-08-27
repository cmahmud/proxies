# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 406
- HTTP: 117 alive / 60 gold
- HTTPS: 175 alive / 13 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40808
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
