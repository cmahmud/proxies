# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 439
- HTTP: 110 alive / 87 gold
- HTTPS: 52 alive / 31 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49434
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
