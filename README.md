# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 445
- HTTP: 102 alive / 84 gold
- HTTPS: 51 alive / 31 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49195
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
