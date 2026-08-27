# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 411
- HTTP: 98 alive / 64 gold
- HTTPS: 154 alive / 19 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 198 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40722
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
