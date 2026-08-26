# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 401
- HTTP: 143 alive / 76 gold
- HTTPS: 181 alive / 27 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40067
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
