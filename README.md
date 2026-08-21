# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 414
- HTTP: 260 alive / 90 gold
- HTTPS: 186 alive / 26 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 247 alive / 161 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29061
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
