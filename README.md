# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 460
- HTTP: 128 alive / 92 gold
- HTTPS: 56 alive / 28 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49424
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
