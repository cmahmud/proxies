# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 473
- HTTP: 167 alive / 102 gold
- HTTPS: 119 alive / 39 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45210
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
