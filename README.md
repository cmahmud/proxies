# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 426
- HTTP: 94 alive / 67 gold
- HTTPS: 47 alive / 28 gold
- SOCKS4: 187 alive / 168 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49047
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
