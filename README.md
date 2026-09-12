# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 456
- HTTP: 124 alive / 96 gold
- HTTPS: 52 alive / 33 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49322
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
