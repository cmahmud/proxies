# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 407
- HTTP: 288 alive / 81 gold
- HTTPS: 155 alive / 22 gold
- SOCKS4: 245 alive / 161 gold
- SOCKS5: 243 alive / 143 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29618
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
