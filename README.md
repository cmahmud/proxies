# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 408
- HTTP: 254 alive / 87 gold
- HTTPS: 174 alive / 23 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29053
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
