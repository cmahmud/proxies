# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 393
- HTTP: 109 alive / 67 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48086
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
