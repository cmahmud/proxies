# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 376
- HTTP: 91 alive / 61 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 174307
- Ever alive: 33081
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
