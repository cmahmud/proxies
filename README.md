# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 401
- HTTP: 148 alive / 73 gold
- HTTPS: 174 alive / 26 gold
- SOCKS4: 164 alive / 147 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40027
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
