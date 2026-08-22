# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 392
- HTTP: 263 alive / 84 gold
- HTTPS: 183 alive / 24 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 248 alive / 147 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31971
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
