# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 445
- HTTP: 120 alive / 90 gold
- HTTPS: 54 alive / 29 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49304
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
