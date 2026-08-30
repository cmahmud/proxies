# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 440
- HTTP: 116 alive / 77 gold
- HTTPS: 120 alive / 33 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44634
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
