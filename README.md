# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 370
- HTTP: 97 alive / 50 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 189 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33028
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
