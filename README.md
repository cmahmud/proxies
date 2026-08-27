# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 411
- HTTP: 100 alive / 64 gold
- HTTPS: 174 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40710
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
