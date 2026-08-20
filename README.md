# SyndProxy private pool

## Current pool

- Alive now: 1471
- Gold now: 559
- HTTP: 617 alive / 189 gold
- HTTPS: 412 alive / 95 gold
- SOCKS4: 226 alive / 143 gold
- SOCKS5: 216 alive / 132 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22807
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
