# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 438
- HTTP: 120 alive / 81 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34224
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
