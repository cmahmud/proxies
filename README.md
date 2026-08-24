# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 400
- HTTP: 113 alive / 66 gold
- HTTPS: 55 alive / 11 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
