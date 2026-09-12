# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 352
- HTTP: 85 alive / 61 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 143 alive / 129 gold
- SOCKS5: 160 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49557
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
