# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 392
- HTTP: 70 alive / 56 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42846
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
