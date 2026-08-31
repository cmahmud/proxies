# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 453
- HTTP: 125 alive / 84 gold
- HTTPS: 88 alive / 35 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 212 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45353
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
