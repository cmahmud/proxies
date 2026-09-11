# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 437
- HTTP: 104 alive / 77 gold
- HTTPS: 58 alive / 27 gold
- SOCKS4: 188 alive / 164 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49123
- Ever gold: 1574

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
