# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 422
- HTTP: 128 alive / 83 gold
- HTTPS: 93 alive / 28 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44040
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
