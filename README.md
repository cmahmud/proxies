# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 423
- HTTP: 101 alive / 72 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48945
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
