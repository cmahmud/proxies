# SyndProxy validated proxy pool

## Current pool

- Alive now: 400
- Gold now: 346
- HTTP: 102 alive / 73 gold
- HTTPS: 41 alive / 25 gold
- SOCKS4: 80 alive / 77 gold
- SOCKS5: 177 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48678
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
