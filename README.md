# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 421
- HTTP: 97 alive / 71 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48945
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
