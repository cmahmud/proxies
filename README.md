# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 443
- HTTP: 124 alive / 83 gold
- HTTPS: 73 alive / 26 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 181 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34717
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
