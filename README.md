# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 404
- HTTP: 87 alive / 61 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48819
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
