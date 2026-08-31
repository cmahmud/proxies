# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 474
- HTTP: 161 alive / 102 gold
- HTTPS: 120 alive / 36 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45195
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
