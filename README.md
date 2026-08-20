# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 396
- HTTP: 175 alive / 73 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 228 alive / 147 gold
- SOCKS5: 221 alive / 155 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26023
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
