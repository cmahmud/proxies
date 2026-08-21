# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 443
- HTTP: 282 alive / 87 gold
- HTTPS: 190 alive / 31 gold
- SOCKS4: 228 alive / 158 gold
- SOCKS5: 275 alive / 167 gold

## Historical pool

- Discovered: 153852
- Ever alive: 28890
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
