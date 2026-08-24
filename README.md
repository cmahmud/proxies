# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 436
- HTTP: 143 alive / 85 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34429
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
