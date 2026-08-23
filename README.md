# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 362
- HTTP: 65 alive / 40 gold
- HTTPS: 26 alive / 11 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 173 alive / 156 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33023
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
