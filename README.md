# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 439
- HTTP: 118 alive / 82 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34245
- Ever gold: 1254

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
