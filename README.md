# SyndProxy validated proxy pool

## Current pool

- Alive now: 400
- Gold now: 346
- HTTP: 93 alive / 72 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 87 alive / 83 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48684
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
