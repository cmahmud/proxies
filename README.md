# SyndProxy validated proxy pool

## Current pool

- Alive now: 721
- Gold now: 455
- HTTP: 174 alive / 85 gold
- HTTPS: 127 alive / 34 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 242 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45339
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
