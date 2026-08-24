# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 440
- HTTP: 121 alive / 83 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34245
- Ever gold: 1254

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
