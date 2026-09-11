# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 378
- HTTP: 91 alive / 65 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 153 alive / 122 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48740
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
