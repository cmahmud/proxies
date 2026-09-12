# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 440
- HTTP: 112 alive / 88 gold
- HTTPS: 56 alive / 30 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49432
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
