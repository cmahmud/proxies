# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 364
- HTTP: 83 alive / 60 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 158 alive / 137 gold
- SOCKS5: 164 alive / 151 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49559
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
