# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 413
- HTTP: 228 alive / 84 gold
- HTTPS: 171 alive / 20 gold
- SOCKS4: 214 alive / 155 gold
- SOCKS5: 221 alive / 154 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27490
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
