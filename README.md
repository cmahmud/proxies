# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 437
- HTTP: 109 alive / 85 gold
- HTTPS: 53 alive / 31 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49430
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
